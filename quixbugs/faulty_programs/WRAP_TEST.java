package faulty_programs;

import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

public class WRAP_TEST {
    @org.junit.Test(timeout = 3000)
    public void test_0() throws Exception {
        java.util.ArrayList result = WRAP.wrap((String) "The leaves did not stir on the trees, grasshoppers chirruped, and the monotonous hollow sound of the sea rising up from below, spoke of the peace, of the eternal sleep awaiting us. So it must have sounded when there was no Yalta, no Oreanda here; so it sounds now, and it will sound as indifferently and monotonously when we are all no more. And in this constancy, in this complete indifference to the life and death of each of us, there lies hid, perhaps, a pledge of our eternal salvation, of the unceasing movement of life upon earth, of unceasing progress towards perfection. Sitting beside a young woman who in the dawn seemed so lovely, soothed and spellbound in these magical surroundings - the sea, mountains, clouds, the open sky - Gurov thought how in reality everything is beautiful in this world when one reflects: everything except what we think or do ourselves when we forget our human dignity and the higher aims of our existence.", (int) 50);
        String resultFormatted = QuixFixOracleHelper.format(result, true);
        assertEquals("[Theleavesdidnotstironthetrees,grasshoppers,chirruped,andthemonotonoushollowsoundofthe,searisingupfrombelow,spokeofthepeace,of,theeternalsleepawaitingus.Soitmusthave,soundedwhentherewasnoYalta,noOreandahere;,soitsoundsnow,anditwillsoundas,indifferentlyandmonotonouslywhenweareallno,more.Andinthisconstancy,inthiscomplete,indifferencetothelifeanddeathofeachofus,,therelieshid,perhaps,apledgeofoureternal,salvation,oftheunceasingmovementoflifeupon,earth,ofunceasingprogresstowardsperfection.,Sittingbesideayoungwomanwhointhedawn,seemedsolovely,soothedandspellboundinthese,magicalsurroundings-thesea,mountains,,clouds,theopensky-Gurovthoughthowin,realityeverythingisbeautifulinthisworld,whenonereflects:everythingexceptwhatwe,thinkordoourselveswhenweforgetourhuman,dignityandthehigheraimsofourexistence.]", resultFormatted);
    }

    @org.junit.Test(timeout = 3000)
    public void test_1() throws Exception {
        java.util.ArrayList result = WRAP.wrap((String) "The leaves did not stir on the trees, grasshoppers chirruped, and the monotonous hollow sound of the sea rising up from below, spoke of the peace, of the eternal sleep awaiting us. So it must have sounded when there was no Yalta, no Oreanda here; so it sounds now, and it will sound as indifferently and monotonously when we are all no more. And in this constancy, in this complete indifference to the life and death of each of us, there lies hid, perhaps, a pledge of our eternal salvation, of the unceasing movement of life upon earth, of unceasing progress towards perfection. Sitting beside a young woman who in the dawn seemed so lovely, soothed and spellbound in these magical surroundings - the sea, mountains, clouds, the open sky - Gurov thought how in reality everything is beautiful in this world when one reflects: everything except what we think or do ourselves when we forget our human dignity and the higher aims of our existence.", (int) 20);
        String resultFormatted = QuixFixOracleHelper.format(result, true);
        assertEquals("[Theleavesdidnot,stironthetrees,,grasshoppers,chirruped,andthe,monotonoushollow,soundofthesea,risingupfrom,below,spokeofthe,peace,ofthe,eternalsleep,awaitingus.Soit,musthavesounded,whentherewasno,Yalta,noOreanda,here;soitsounds,now,anditwill,soundas,indifferentlyand,monotonouslywhen,weareallnomore.,Andinthis,constancy,inthis,complete,indifferencetothe,lifeanddeathof,eachofus,there,lieshid,perhaps,,apledgeofour,eternalsalvation,,oftheunceasing,movementoflife,uponearth,of,unceasingprogress,towardsperfection.,Sittingbesidea,youngwomanwhoin,thedawnseemedso,lovely,soothedand,spellboundinthese,magical,surroundings-the,sea,mountains,,clouds,theopen,sky-Gurovthought,howinreality,everythingis,beautifulinthis,worldwhenone,reflects:,everythingexcept,whatwethinkordo,ourselveswhenwe,forgetourhuman,dignityandthe,higheraimsofour,existence.]", resultFormatted);
    }

    @org.junit.Test(timeout = 3000)
    public void test_2() throws Exception {
        java.util.ArrayList result = WRAP.wrap((String) "The leaves did not stir on the trees, grasshoppers chirruped, and the monotonous hollow sound of the sea rising up from below, spoke of the peace, of the eternal sleep awaiting us. So it must have sounded when there was no Yalta, no Oreanda here; so it sounds now, and it will sound as indifferently and monotonously when we are all no more. And in this constancy, in this complete indifference to the life and death of each of us, there lies hid, perhaps, a pledge of our eternal salvation, of the unceasing movement of life upon earth, of unceasing progress towards perfection. Sitting beside a young woman who in the dawn seemed so lovely, soothed and spellbound in these magical surroundings - the sea, mountains, clouds, the open sky - Gurov thought how in reality everything is beautiful in this world when one reflects: everything except what we think or do ourselves when we forget our human dignity and the higher aims of our existence.", (int) 80);
        String resultFormatted = QuixFixOracleHelper.format(result, true);
        assertEquals("[Theleavesdidnotstironthetrees,grasshopperschirruped,andthemonotonous,hollowsoundofthesearisingupfrombelow,spokeofthepeace,ofthe,eternalsleepawaitingus.SoitmusthavesoundedwhentherewasnoYalta,no,Oreandahere;soitsoundsnow,anditwillsoundasindifferentlyand,monotonouslywhenweareallnomore.Andinthisconstancy,inthiscomplete,indifferencetothelifeanddeathofeachofus,therelieshid,perhaps,a,pledgeofoureternalsalvation,oftheunceasingmovementoflifeuponearth,,ofunceasingprogresstowardsperfection.Sittingbesideayoungwomanwhoin,thedawnseemedsolovely,soothedandspellboundinthesemagicalsurroundings,-thesea,mountains,clouds,theopensky-Gurovthoughthowinreality,everythingisbeautifulinthisworldwhenonereflects:everythingexceptwhat,wethinkordoourselveswhenweforgetourhumandignityandthehigheraims,ofourexistence.]", resultFormatted);
    }

    @org.junit.Test(timeout = 3000)
    public void test_3() throws Exception {
        java.util.ArrayList result = WRAP.wrap((String) "The leaves did not stir on the trees, grasshoppers chirruped, and the monotonous hollow sound of the sea rising up from below, spoke of the peace, of the eternal sleep awaiting us. So it must have sounded when there was no Yalta, no Oreanda here; so it sounds now, and it will sound as indifferently and monotonously when we are all no more. And in this constancy, in this complete indifference to the life and death of each of us, there lies hid, perhaps, a pledge of our eternal salvation, of the unceasing movement of life upon earth, of unceasing progress towards perfection. Sitting beside a young woman who in the dawn seemed so lovely, soothed and spellbound in these magical surroundings - the sea, mountains, clouds, the open sky - Gurov thought how in reality everything is beautiful in this world when one reflects: everything except what we think or do ourselves when we forget our human dignity and the higher aims of our existence.", (int) 77);
        String resultFormatted = QuixFixOracleHelper.format(result, true);
        assertEquals("[Theleavesdidnotstironthetrees,grasshopperschirruped,andthe,monotonoushollowsoundofthesearisingupfrombelow,spokeofthepeace,,oftheeternalsleepawaitingus.Soitmusthavesoundedwhentherewasno,Yalta,noOreandahere;soitsoundsnow,anditwillsoundasindifferently,andmonotonouslywhenweareallnomore.Andinthisconstancy,inthis,completeindifferencetothelifeanddeathofeachofus,therelieshid,,perhaps,apledgeofoureternalsalvation,oftheunceasingmovementof,lifeuponearth,ofunceasingprogresstowardsperfection.Sittingbesidea,youngwomanwhointhedawnseemedsolovely,soothedandspellboundin,thesemagicalsurroundings-thesea,mountains,clouds,theopensky-,Gurovthoughthowinrealityeverythingisbeautifulinthisworldwhenone,reflects:everythingexceptwhatwethinkordoourselveswhenweforgetour,humandignityandthehigheraimsofourexistence.]", resultFormatted);
    }

    @org.junit.Test(timeout = 3000)
    public void test_4() throws Exception {
        java.util.ArrayList result = WRAP.wrap((String) "The leaves did not stir on the trees, grasshoppers chirruped, and the monotonous hollow sound of the sea rising up from below, spoke of the peace, of the eternal sleep awaiting us. So it must have sounded when there was no Yalta, no Oreanda here; so it sounds now, and it will sound as indifferently and monotonously when we are all no more. And in this constancy, in this complete indifference to the life and death of each of us, there lies hid, perhaps, a pledge of our eternal salvation, of the unceasing movement of life upon earth, of unceasing progress towards perfection. Sitting beside a young woman who in the dawn seemed so lovely, soothed and spellbound in these magical surroundings - the sea, mountains, clouds, the open sky - Gurov thought how in reality everything is beautiful in this world when one reflects: everything except what we think or do ourselves when we forget our human dignity and the higher aims of our existence.", (int) 140);
        String resultFormatted = QuixFixOracleHelper.format(result, true);
        assertEquals("[Theleavesdidnotstironthetrees,grasshopperschirruped,andthemonotonoushollowsoundofthesearisingupfrombelow,spokeofthe,peace,oftheeternalsleepawaitingus.SoitmusthavesoundedwhentherewasnoYalta,noOreandahere;soitsoundsnow,anditwill,soundasindifferentlyandmonotonouslywhenweareallnomore.Andinthisconstancy,inthiscompleteindifferencetothelifeanddeath,ofeachofus,therelieshid,perhaps,apledgeofoureternalsalvation,oftheunceasingmovementoflifeuponearth,ofunceasing,progresstowardsperfection.Sittingbesideayoungwomanwhointhedawnseemedsolovely,soothedandspellboundinthesemagical,surroundings-thesea,mountains,clouds,theopensky-Gurovthoughthowinrealityeverythingisbeautifulinthisworldwhenone,reflects:everythingexceptwhatwethinkordoourselveswhenweforgetourhumandignityandthehigheraimsofourexistence.]", resultFormatted);
    }

    // EVOSUITE

    @Test(timeout = 4000)
    public void test_5() throws Throwable {
        WRAP wRAP0 = new WRAP();
    }

    @Test(timeout = 4000)
    public void test_6() throws Throwable {
        String[] stringArray0 = new String[4];
        WRAP.main(stringArray0);
        assertEquals(4, stringArray0.length);
    }

    @Test(timeout = 4000)
    public void test_7() throws Throwable {
        // Undeclared exception!
        try {
            WRAP.wrap("", (-400));
            fail("Expecting exception: StringIndexOutOfBoundsException");
        } catch (StringIndexOutOfBoundsException e) {
        }
    }

    @Test(timeout = 4000)
    public void test_8() throws Throwable {
        ArrayList<String> arrayList0 = WRAP.wrap("B1K\n*B9\"!F ", 1);
        assertEquals(11, arrayList0.size());
    }

    @Test(timeout = 4000)
    public void test_9() throws Throwable {
        // Undeclared exception!
        try {
            WRAP.wrap((String) null, 3912);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
        }
    }

    @Test(timeout = 4000)
    public void test_10() throws Throwable {
        ArrayList<String> arrayList0 = WRAP.wrap("1\"NbV6uxjn@}l..f+U8", 3674);
        assertEquals(1, arrayList0.size());
    }

}

